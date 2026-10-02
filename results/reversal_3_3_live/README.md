# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-02 14:50:06 EDT`
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

- Cash: `$41,269.30`
- Equity: `$81,364.30`
- Realized PnL: `$71,364.30`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode        instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
    ZS     option         option ZS261120C00200000       2026-10-02                   0     27     40095.0                 40095.0        14.85          14.85      196.86        196.86          bid_ask_mid                      14.85                bid_ask_mid                    True             0.0                    0.0         94.59               37              0.97         55.98           55.98                   77.3                 818.0          103.0               0.04                      ok
```

## Today's Closed Trades (2026-10-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS           94.59               37            0.97              1.34        198.20                77.30         0.642            pass              0.679             15.0                           0.229               -0.23             -0.512                                 ok            True                  False
  DRAM           80.65               31            0.85              0.37         61.87                54.09         0.573            pass              0.342             42.4                           0.356                3.17             -0.009                                 ok            True                  False
  AMGN           83.33               24            0.94              2.69        406.12                47.14         0.528            pass              0.318             27.7                           0.391                4.61              0.511                                 ok            True                  False
  MSTR           88.00               25            2.71              3.05        159.19                96.54         0.514            pass              0.382              5.6                           0.126                1.45             -0.466                                 ok            True                  False
   TRI           84.62               26            1.64              1.14         98.87                57.35         0.511            pass              0.472             63.8                           0.380                3.54              0.283                                 ok            True                  False
    MU           92.31               26            1.90             14.62       1091.12                49.88         0.504            pass              0.538             17.7                           0.339                5.98              0.333                                 ok            True                  False
  SNPS           80.95               42            0.35              1.19        490.03                58.70         0.528            pass              0.506             75.8                           0.639               26.98              1.970                                 ok           False                  False
  TEAM          100.00               34            1.37              1.82        189.13                55.53         0.519            pass              0.673             20.4                           0.335               -2.45             -0.617           downtrend_blocked_streak           False                  False
  PAYX           73.33               15            1.82              1.29        100.29                39.54         0.517            pass              0.112              8.9                           0.332              -14.76             -1.728 downtrend_blocked_slope_and_streak           False                  False
  ADBE           87.50               32            1.15              1.94        240.45                44.30         0.494 below_threshold              0.508             37.2                           0.565               -4.18             -0.385            downtrend_blocked_slope           False                  False
  CTSH          100.00                6            3.44              1.47         60.25                46.07         0.488 below_threshold              0.456              2.6                           0.144               -1.81             -0.129                                 ok           False                  False
  ISRG           83.33               12            2.00              5.62        398.83                28.38         0.484 below_threshold              0.158              2.6                           0.148               -0.03              0.122                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-10-02T14:50:06.331180-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"allocated_cash": 40095.0, "asset_type": "option", "contract_symbol": "ZS261120C00200000", "contracts": 27, "early_entry_score": 0.679, "entry_mode": "regular", "entry_option_price": 14.85, "execution_mode": "option", "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 818.0, "option_spread_pct": 4.04, "option_volume": 103.0, "success_rate": 94.59, "ticker": "ZS", "timing_score": 0.642}
2026-10-02T14:50:06.331180-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-02", "training_samples": 5912, "window": 5}
2026-10-02T12:00:05.856785-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:55:04.675487-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:50:01.924134-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:45:02.865482-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:40:05.643538-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:35:05.841468-04:00 early_entry_1135 early_entry_shadow {"contract_symbol": "ISRG261120C00400000", "current_drop_pct": 0.61, "early_entry_score": 0.78, "early_reclaim_pct": 62.7, "entry_ask": 23.4, "entry_bid": 21.8, "entry_mode": "early", "entry_option_price": 22.6, "hypothetical_budget": 40682.15, "hypothetical_contracts": 18, "matched_signals": 35, "option_liquidity_status": "low_volume", "option_open_interest": 285.0, "option_spread_pct": 7.08, "option_volume": 15.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.592, "shadow_only": true, "success_rate": 94.29, "ticker": "ISRG", "timing_score": 0.446, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.78, "early_reclaim_pct": 62.7, "matched_signals": 35, "recovery_stability_score": 0.592, "success_rate": 94.29, "ticker": "ISRG", "timing_score": 0.446, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-02T11:30:06.447357-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:25:01.826552-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261002145006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261002145006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261002145006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261002145006)

</details>
