# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-28 14:50:01 EDT`
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

- Cash: `$3,289.30`
- Equity: `$131,804.30`
- Realized PnL: `$122,764.30`
- Unrealized PnL: `$-960.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CSCO     option         option CSCO261218C00110000       2026-10-28                   0     90     65475.0                 65475.0         7.28           7.28      110.47        110.53          bid_ask_mid                       7.28                bid_ask_mid                    True             0.0                    0.0         80.77               26              0.82         42.92           42.80                  35.12                4095.0         1198.0               0.02                      ok
  TEAM     option         option TEAM261218C00230000       2026-10-26                   2     32     64000.0                 63040.0        20.00          19.70      220.60        220.93          bid_ask_mid                      19.70                bid_ask_mid                    True          -960.0                   -1.5        100.00               12              3.08         70.90           70.79                  47.89                 302.0           39.0               0.10                      ok
```

## Today's Closed Trades (2026-10-28)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   KHC           85.71               21            1.14              0.19         23.98                36.33         0.562          pass              0.297              5.1                           0.115                4.78              0.621                      ok            True                  False
  CSCO           80.77               26            0.82              0.64        111.11                35.12         0.533          pass              0.340             53.1                           0.714               -2.79             -0.023                      ok            True                  False
    ZS           91.43               35            0.98              1.78        259.39                56.99         0.530          pass              0.639             38.3                           0.404               16.68              2.351                      ok            True                  False
   PEP           80.00               25            0.67              0.62        133.23                25.80         0.520          pass              0.290             45.9                           0.518                2.58              0.401                      ok            True                  False
  CTAS           93.75               16            1.41              2.11        213.89                26.02         0.511          pass              0.513             18.4                           0.232                1.51              0.377                      ok            True                  False
  CRWD           85.00               40            0.90              1.68        267.30                57.68         0.508          pass              0.516             44.1                           0.505                6.55              1.268                      ok            True                  False
   CSX           82.76               29            0.60              0.22         52.18                27.86         0.508          pass              0.339             29.2                           0.298                7.61              0.908                      ok            True                  False
  TMUS           80.00               25            0.89              0.92        146.44                63.84         0.661          pass              0.366             66.8                           0.452               -7.78             -0.938 downtrend_blocked_slope           False                  False
  MDLZ           87.50                8            1.01              0.44         62.16                25.51         0.613          pass              0.302             13.7                           0.185               -1.36             -0.112                      ok           False                  False
  MSTR           90.70               43            0.03              0.03        141.39                70.33         0.606          pass              0.841             98.5                           0.875               -1.31             -0.099                      ok           False                  False
 CMCSA           88.89                9            1.21              0.19         21.76                26.07         0.576          pass              0.374             26.4                           0.255                2.49              0.226                      ok           False                  False
  MPWR           77.27               44            0.03              0.24       1211.79                59.51         0.551          pass              0.551             98.5                           0.845               -2.54             -0.561                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-10-28T14:50:01.756543-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"allocated_cash": 65475.0, "asset_type": "option", "contract_symbol": "CSCO261218C00110000", "contracts": 90, "early_entry_score": 0.34, "entry_mode": "regular", "entry_option_price": 7.275, "execution_mode": "option", "matched_signals": 26, "option_liquidity_status": "ok", "option_open_interest": 4095.0, "option_spread_pct": 2.06, "option_volume": 1198.0, "success_rate": 80.77, "ticker": "CSCO", "timing_score": 0.533}
2026-10-28T14:50:01.756543-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"early_entry_score": 0.297, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 7.0, "option_spread_pct": 14.29, "option_volume": 11.0, "reason": "no_trade_low_option_liquidity", "ticker": "KHC", "timing_score": 0.562}
2026-10-28T14:50:01.756543-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-28", "training_samples": 6213, "window": 5}
2026-10-28T12:00:04.408643-04:00 early_entry_1200      early_entry_shadow   {"contract_symbol": "ALNY261218C00230000", "current_drop_pct": 0.6, "early_entry_score": 0.709, "early_reclaim_pct": 80.0, "entry_ask": 19.0, "entry_bid": 15.7, "entry_mode": "early", "entry_option_price": 17.35, "hypothetical_budget": 34382.15, "hypothetical_contracts": 19, "matched_signals": 43, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 69.0, "option_spread_pct": 19.02, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.759, "shadow_only": true, "success_rate": 88.37, "ticker": "ALNY", "timing_score": 0.462, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.709, "early_reclaim_pct": 80.0, "matched_signals": 43, "recovery_stability_score": 0.759, "success_rate": 88.37, "ticker": "ALNY", "timing_score": 0.462, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-28T11:55:06.476667-04:00 early_entry_1155      early_entry_shadow {"contract_symbol": "ALNY261218C00230000", "current_drop_pct": 0.51, "early_entry_score": 0.726, "early_reclaim_pct": 83.1, "entry_ask": 19.0, "entry_bid": 15.7, "entry_mode": "early", "entry_option_price": 17.35, "hypothetical_budget": 34382.15, "hypothetical_contracts": 19, "matched_signals": 44, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 69.0, "option_spread_pct": 19.02, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.776, "shadow_only": true, "success_rate": 88.64, "ticker": "ALNY", "timing_score": 0.461, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.726, "early_reclaim_pct": 83.1, "matched_signals": 44, "recovery_stability_score": 0.776, "success_rate": 88.64, "ticker": "ALNY", "timing_score": 0.461, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-28T11:50:06.101583-04:00 early_entry_1150      early_entry_shadow   {"contract_symbol": "ALNY261218C00230000", "current_drop_pct": 0.65, "early_entry_score": 0.697, "early_reclaim_pct": 78.4, "entry_ask": 19.0, "entry_bid": 15.7, "entry_mode": "early", "entry_option_price": 17.35, "hypothetical_budget": 34382.15, "hypothetical_contracts": 19, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 69.0, "option_spread_pct": 19.02, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.755, "shadow_only": true, "success_rate": 88.1, "ticker": "ALNY", "timing_score": 0.465, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.697, "early_reclaim_pct": 78.4, "matched_signals": 42, "recovery_stability_score": 0.755, "success_rate": 88.1, "ticker": "ALNY", "timing_score": 0.465, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-28T11:45:03.424860-04:00 early_entry_1145      early_entry_shadow  {"contract_symbol": "ALNY261218C00230000", "current_drop_pct": 0.57, "early_entry_score": 0.713, "early_reclaim_pct": 81.0, "entry_ask": 18.3, "entry_bid": 15.7, "entry_mode": "early", "entry_option_price": 17.0, "hypothetical_budget": 34382.15, "hypothetical_contracts": 20, "matched_signals": 43, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 69.0, "option_spread_pct": 15.29, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.769, "shadow_only": true, "success_rate": 88.37, "ticker": "ALNY", "timing_score": 0.463, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.713, "early_reclaim_pct": 81.0, "matched_signals": 43, "recovery_stability_score": 0.769, "success_rate": 88.37, "ticker": "ALNY", "timing_score": 0.463, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-28T11:40:06.443481-04:00 early_entry_1140      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-28T11:35:05.885505-04:00 early_entry_1135      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-28T11:30:05.433292-04:00 early_entry_1130      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261028145001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261028145001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261028145001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261028145001)

</details>
