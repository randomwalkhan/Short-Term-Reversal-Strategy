# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-22 09:45:04 EDT`
Last processed slot: `manual`

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
  AVGO     option         option AVGO260717C00420000       2026-05-21                   1      4     12140.0                 12400.0        30.35           31.0      415.18        418.17     last_price_stale                        NaN                unavailable                   False           260.0                   2.14         91.67               36              0.62         50.17            0.39                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    MU           82.35               34            0.79              4.22        760.29                87.43         0.655            pass              0.493             68.1                           0.659                1.24             -0.597                                 ok            True                  False
  SBUX           95.00               20            0.80              0.58        103.88                32.97         0.587            pass              0.670             48.1                           0.372               -0.98             -0.040                                 ok            True                  False
  COST           83.33               12            1.09              8.00       1047.02                22.19         0.553            pass              0.228             23.5                           0.225                3.00              0.586                                 ok            True                  False
   STX           94.87               39            0.15              0.87        810.09                68.63         0.590            pass              0.913             88.1                           0.503                3.40             -0.427                                 ok           False                  False
   WDC           95.12               41            0.20              0.70        486.16                59.01         0.542            pass              0.916             87.4                           0.604                1.14             -0.534                                 ok           False                  False
   WMT           90.32               31            0.47              0.40        121.17                34.61         0.523            pass              0.537             23.0                           0.154               -7.41             -0.479            downtrend_blocked_slope           False                  False
 GOOGL           89.19               37            0.55              1.48        387.02                41.05         0.520            pass              0.587             36.5                           0.270               -3.81             -0.253            downtrend_blocked_slope           False                  False
  GOOG           89.74               39            0.43              1.14        382.98                40.91         0.517            pass              0.634             43.2                           0.283               -3.83             -0.276 downtrend_blocked_slope_and_streak           False                  False
  NVDA           89.74               39            0.24              0.37        219.35                44.83         0.513            pass              0.675             56.9                           0.291                1.76              0.018                                 ok           False                  False
  REGN           95.56               45            0.00              0.01        642.59                49.06         0.509            pass              0.951             99.9                           0.658               -9.98             -1.493 downtrend_blocked_slope_and_streak           False                  False
  DXCM           81.82               44            0.24              0.12         71.85                51.37         0.490 below_threshold              0.527             76.4                           0.455               18.35              2.240                                 ok           False                  False
   CSX           87.18               39            0.16              0.05         45.88                20.37         0.435 below_threshold              0.653             75.0                           0.359                2.22              0.351                                 ok           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260522094504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260522094504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260522094504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260522094504)

</details>
