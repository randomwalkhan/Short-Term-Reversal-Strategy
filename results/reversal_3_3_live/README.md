# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-02 15:05:02 EDT`
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
- Equity: `$80,756.80`
- Realized PnL: `$71,364.30`
- Unrealized PnL: `$-607.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode        instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
    ZS     option         option ZS261120C00200000       2026-10-02                   0     27     40095.0                 39487.5        14.85          14.62      196.86        196.56          bid_ask_mid                      14.62                bid_ask_mid                    True          -607.5                  -1.52         94.59               37              0.97         55.98            55.8                   77.3                 818.0          103.0               0.04                      ok
```

## Today's Closed Trades (2026-10-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS           94.59               37            1.12              1.55        198.11                77.30         0.633            pass              0.638              1.8                           0.108               -0.38             -0.519                                 ok            True                  False
  DRAM           80.65               31            0.80              0.35         61.88                54.09         0.576            pass              0.353             46.2                           0.461                3.23             -0.006                                 ok            True                  False
  MSTR           89.29               28            2.06              2.31        159.51                96.54         0.538            pass              0.507             28.4                           0.452                2.13             -0.436                                 ok            True                  False
  AMGN           84.62               26            0.76              2.16        406.35                47.14         0.530            pass              0.409             42.0                           0.537                4.81              0.519                                 ok            True                  False
  SNPS           80.00               40            0.59              2.01        489.68                58.70         0.524            pass              0.430             59.1                           0.443               26.68              1.959                                 ok            True                  False
   TRI           84.00               25            1.71              1.19         98.85                57.35         0.512            pass              0.445             62.2                           0.387                3.46              0.280                                 ok            True                  False
    MU           92.31               26            1.91             14.66       1091.11                49.88         0.504            pass              0.538             17.4                           0.422                5.97              0.333                                 ok            True                  False
  INTC           87.50               40            0.27              0.22        119.90                73.87         0.608            pass              0.569             36.0                           0.362               10.20              0.120                                 ok           False                  False
  PAYX           73.33               15            1.72              1.21        100.32                39.54         0.524            pass              0.129             14.4                           0.437              -14.66             -1.723 downtrend_blocked_slope_and_streak           False                  False
  TEAM          100.00               34            1.32              1.75        189.16                55.53         0.522            pass              0.683             23.5                           0.361               -2.40             -0.614           downtrend_blocked_streak           False                  False
   ADP          100.00                5            2.24              4.14        262.18                23.86         0.486 below_threshold              0.469              6.8                           0.361               -4.86             -0.445 downtrend_blocked_slope_and_streak           False                  False
  ADBE           88.57               35            1.10              1.86        240.48                44.30         0.480 below_threshold              0.562             39.7                           0.564               -4.14             -0.383                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-10-02T15:05:02.993202-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-10-02T15:00:05.745060-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-10-02T14:55:02.797853-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-10-02T14:50:06.331180-04:00       entry_1500              entry {"allocated_cash": 40095.0, "asset_type": "option", "contract_symbol": "ZS261120C00200000", "contracts": 27, "early_entry_score": 0.679, "entry_mode": "regular", "entry_option_price": 14.85, "execution_mode": "option", "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 818.0, "option_spread_pct": 4.04, "option_volume": 103.0, "success_rate": 94.59, "ticker": "ZS", "timing_score": 0.642}
2026-10-02T14:50:06.331180-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                       {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-02", "training_samples": 5912, "window": 5}
2026-10-02T12:00:05.856785-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:55:04.675487-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:50:01.924134-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:45:02.865482-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:40:05.643538-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261002150502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261002150502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261002150502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261002150502)

</details>
