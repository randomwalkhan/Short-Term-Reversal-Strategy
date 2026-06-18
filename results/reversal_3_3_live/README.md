# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-18 14:50:01 EDT`
Last processed slot: `entry_1500`

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

- Cash: `$13,462.50`
- Equity: `$26,514.50`
- Realized PnL: `$16,514.50`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   WMT     option         option WMT260724C00120000       2026-06-18                   0     52     13052.0                 13052.0         2.51           2.51      117.33        117.33          bid_ask_mid                       2.51                bid_ask_mid                    True             0.0                    0.0         86.21               29              0.68         25.57           25.57                  34.58                 124.0           47.0               0.14                      ok
```

## Today's Closed Trades (2026-06-18)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   WMT           86.21               29            0.68              0.56        117.89                34.58         0.549          pass              0.467             40.1                           0.569               -0.35              0.021                                 ok            True                  False
  CRWD           87.18               39            0.52              2.47        681.90                64.33         0.541          pass              0.691             84.0                           0.590               -5.51              0.069                                 ok            True                  False
  MDLZ           95.24               21            0.90              0.38         60.70                21.28         0.523          pass              0.640             38.2                           0.478               -1.11             -0.155                                 ok            True                  False
  INTU           76.47               34            1.33              2.51        268.00                98.62         0.682          pass              0.419             63.6                           0.547              -12.08             -1.270 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                3            1.21              0.20         23.12                27.50         0.672          pass              0.517             16.7                           0.325                3.85              0.378                                 ok           False                  False
  AMGN           83.33                6            1.78              4.26        339.83                27.62         0.572          pass              0.206             20.0                           0.415               -2.90             -0.124           downtrend_blocked_streak           False                  False
   TRI           77.27               22            1.44              0.80         78.91                52.51         0.565          pass              0.279             47.5                           0.293               -8.90             -0.837 downtrend_blocked_slope_and_streak           False                  False
  TEAM           88.10               42            0.65              0.39         84.22                82.55         0.557          pass              0.709             79.0                           0.585              -17.40             -1.868 downtrend_blocked_slope_and_streak           False                  False
  GILD           87.50                8            1.87              1.64        124.75                29.17         0.548          pass              0.322             22.5                           0.438               -4.07             -0.247           downtrend_blocked_streak           False                  False
  WDAY           83.33               18            2.96              2.53        120.75                69.08         0.544          pass              0.247             16.6                           0.147              -20.07             -2.165 downtrend_blocked_slope_and_streak           False                  False
   AEP           77.27               22            0.41              0.37        128.11                19.26         0.529          pass              0.325             63.9                           0.399               -0.04              0.064                                 ok           False                  False
   XEL          100.00               16            0.46              0.25         77.35                22.61         0.528          pass              0.603             36.8                           0.240               -0.11              0.077                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-06-18T14:50:01.395672-04:00       entry_1500              entry {"allocated_cash": 13052.0, "asset_type": "option", "contract_symbol": "WMT260724C00120000", "contracts": 52, "early_entry_score": 0.467, "entry_mode": "regular", "entry_option_price": 2.51, "execution_mode": "option", "matched_signals": 29, "option_liquidity_status": "ok", "option_open_interest": 124.0, "option_spread_pct": 13.55, "option_volume": 47.0, "success_rate": 86.21, "ticker": "WMT", "timing_score": 0.549}
2026-06-18T14:50:01.395672-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-18", "training_samples": 5252, "window": 5}
2026-06-18T12:00:02.352957-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:55:04.331586-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:50:03.235877-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:45:01.152442-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:40:06.149608-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:35:05.166451-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:30:05.153206-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:25:04.328726-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260618145001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260618145001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260618145001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260618145001)

</details>
