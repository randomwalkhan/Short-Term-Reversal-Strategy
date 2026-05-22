# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-22 09:55:05 EDT`
Last processed slot: `manage_1000`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$16,177.75`
- Equity: `$28,577.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$260.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-21                   1      4     12140.0                 12400.0        30.35           31.0      415.18        415.51     last_price_stale                        NaN                unavailable                   False           260.0                   2.14         91.67               36              0.62         50.17            0.78                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    MU           81.82               33            1.26              6.74        759.21                87.43         0.632          pass              0.412             49.1                           0.419                0.76             -0.619                                 ok            True                  False
  SBUX           93.33               15            1.06              0.77        103.80                32.97         0.602          pass              0.544             31.7                           0.227               -1.24             -0.052                                 ok            True                  False
  COST           83.33               12            1.11              8.13       1046.97                22.19         0.552          pass              0.224             22.3                           0.205                2.98              0.585                                 ok            True                  False
  CHTR           89.19               37            0.87              0.91        148.51               115.38         0.514          pass              0.572             31.8                           0.252               -4.68             -0.302                                 ok            True                  False
  NVDA           87.88               33            0.76              1.17        219.01                44.83         0.514          pass              0.463             16.1                           0.140                1.23             -0.006                                 ok            True                  False
  INSM           80.85               47            0.05              0.03        109.52               111.27         0.744          pass              0.591             97.8                           0.570                8.02              0.106                                 ok           False                  False
  MSTR           90.24               41            0.09              0.11        164.80                63.46         0.586          pass              0.805             91.2                           0.691              -12.20             -1.757            downtrend_blocked_slope           False                  False
   STX           94.87               39            0.28              1.56        809.79                68.63         0.583          pass              0.884             78.7                           0.423                3.27             -0.432                                 ok           False                  False
   WMT           93.33               15            1.18              1.00        120.91                34.61         0.582          pass              0.482             11.7                           0.187               -8.07             -0.511            downtrend_blocked_slope           False                  False
   WDC           95.12               41            0.01              0.05        486.44                59.01         0.554          pass              0.953             99.1                           0.650                1.33             -0.526                                 ok           False                  False
  REGN           94.12               34            0.54              2.41        641.56                49.06         0.547          pass              0.852             87.0                           0.542              -10.46             -1.517 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           89.19               37            0.51              1.38        387.07                41.05         0.523          pass              0.600             41.0                           0.272               -3.77             -0.251            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-05-22T00:00:04.747847-04:00     data_refresh   data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 92}
2026-05-21T15:10:07.725283-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-05-21T15:05:09.016170-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-05-21T15:00:06.517867-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-05-21T14:55:08.024423-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-05-21T14:50:05.768088-04:00       entry_1500  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-21T14:50:05.768088-04:00       entry_1500 timing_overlay                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-21", "training_samples": 5058, "window": 5}
2026-05-21T12:00:02.068266-04:00 early_entry_1200  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-21T11:55:01.035616-04:00 early_entry_1155  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-21T11:50:01.038543-04:00 early_entry_1150          entry {"allocated_cash": 12140.0, "asset_type": "option", "contract_symbol": "AVGO260717C00420000", "contracts": 4, "early_entry_score": 0.724, "entry_mode": "early", "entry_option_price": 30.35, "execution_mode": "option", "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 2101.0, "option_spread_pct": 2.97, "option_volume": 296.0, "success_rate": 91.67, "ticker": "AVGO", "timing_score": 0.497}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260522095505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260522095505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260522095505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260522095505)

</details>
