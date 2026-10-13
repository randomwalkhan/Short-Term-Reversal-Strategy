# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-13 09:35:01 EDT`
Last processed slot: `manage_0930`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
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

- Cash: `$1,059.30`
- Equity: `$119,364.30`
- Realized PnL: `$107,274.30`
- Unrealized PnL: `$2,090.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CTSH     option         option CTSH261120C00060000       2026-10-09                   2    160     58400.0                 60800.0         3.65           3.80       59.31         61.62     last_price_stale                        NaN                unavailable                   False          2400.0                   4.11         93.10               29              1.17         50.42             0.0                  46.57                 209.0           38.0               0.08                      ok
   CEG     option         option  CEG261120C00290000       2026-10-12                   1     31     57815.0                 57505.0        18.65          18.55      291.07        290.39     last_price_stale                        NaN                unavailable                   False          -310.0                  -0.54         83.33               12              2.35         48.77             0.0                  62.49                 920.0          121.0               0.05                      ok
```

## Today's Closed Trades (2026-10-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           87.50               24            1.19              2.44        292.84                56.17         0.570            pass              0.508             52.4                           0.602                9.76              1.625                                 ok            True                  False
  CSCO           87.50               16            1.14              0.92        114.95                34.19         0.556            pass              0.443             49.2                           0.416                7.04              0.896                                 ok            True                  False
  SNPS           86.84               38            0.56              1.96        501.67                52.43         0.540            pass              0.660             79.0                           0.890               20.39              1.529                                 ok            True                  False
  MSTR           92.31               39            0.03              0.03        152.67                78.93         0.658            pass              0.837             83.3                           0.405               -1.31             -0.340                                 ok           False                  False
  META           84.38               32            0.40              2.09        742.07                52.81         0.622            pass              0.555             76.6                           0.758                0.16              0.024                                 ok           False                  False
  QCOM           90.00               40            0.03              0.04        174.41                55.62         0.590            pass              0.820             98.0                           0.828               -5.29             -0.650 downtrend_blocked_slope_and_streak           False                  False
  MPWR           88.46               26            1.15             10.58       1314.70                51.39         0.559            pass              0.559             56.9                           0.523               -3.68             -0.321            downtrend_blocked_slope           False                  False
  SHOP           78.95               19            1.86              2.33        178.22                48.43         0.553            pass              0.230             38.4                           0.457               18.63              2.022                                 ok           False                  False
  INTC           81.82               22            2.77              1.97        100.51                67.41         0.551            pass              0.208              8.2                           0.202              -15.00             -1.953 downtrend_blocked_slope_and_streak           False                  False
  UPRO           83.78               37            0.16              0.18        155.37                28.94         0.508            pass              0.552             73.4                           0.534                4.89              0.599                                 ok           False                  False
  CDNS           78.95               19            1.62              3.94        346.73                33.13         0.505            pass              0.148             12.6                           0.166                5.74              0.459                                 ok           False                  False
  NVDA           88.24               17            1.36              2.15        225.40                22.13         0.499 below_threshold              0.316              0.0                           0.230               -1.74             -0.164           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-10-13T00:00:05.318337-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                           {'saved': 91, 'empty': 2}
2026-10-12T15:10:05.555878-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-10-12T15:05:06.325460-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-10-12T15:00:05.898503-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-10-12T14:55:06.164837-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-10-12T14:50:02.373216-04:00       entry_1500              entry {"allocated_cash": 57815.0, "asset_type": "option", "contract_symbol": "CEG261120C00290000", "contracts": 31, "early_entry_score": 0.18, "entry_mode": "regular", "entry_option_price": 18.65, "execution_mode": "option", "matched_signals": 12, "option_liquidity_status": "ok", "option_open_interest": 920.0, "option_spread_pct": 4.83, "option_volume": 121.0, "success_rate": 83.33, "ticker": "CEG", "timing_score": 0.545}
2026-10-12T14:50:02.373216-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-12", "training_samples": 6005, "window": 5}
2026-10-12T12:00:04.227731-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T11:55:04.380745-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T11:50:05.333973-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261013093501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261013093501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261013093501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261013093501)

</details>
