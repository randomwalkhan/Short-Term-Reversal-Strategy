# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-28 15:35:06 EDT`
Last processed slot: `manage_1530`

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

- Cash: `$26,688.10`
- Equity: `$53,440.60`
- Realized PnL: `$42,788.10`
- Unrealized PnL: `$652.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SHOP     option         option SHOP261016C00155000       2026-08-28                   0     29     26100.0                 26752.5          9.0           9.23      153.02        153.06          bid_ask_mid                       9.23                bid_ask_mid                    True           652.5                    2.5         94.59               37              0.85         45.17           45.58                  69.26                 763.0          153.0               0.07                      ok
```

## Today's Closed Trades (2026-08-28)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  SHOP           94.59               37            0.82              0.89        153.95                69.26         0.619          pass              0.696             21.6                           0.261               -0.82              0.272                      ok            True                  False
  AMGN          100.00               12            1.21              3.70        435.40                27.65         0.599          pass              0.520             15.6                           0.416                4.58              0.521                      ok            True                  False
   MAR           96.55               29            0.59              1.46        353.24                33.75         0.561          pass              0.678             31.7                           0.420               -1.18             -0.057                      ok            True                  False
  REGN          100.00               10            1.65              9.31        803.72                24.94         0.537          pass              0.604             50.1                           0.607               -1.01             -0.033                      ok            True                  False
  GILD          100.00               10            2.28              2.38        147.84                26.47         0.525          pass              0.496             14.5                           0.479                5.14              0.601                      ok            True                  False
  VRTX           96.67               30            1.00              3.82        545.91                32.96         0.519          pass              0.708             40.9                           0.448                7.19              0.646                      ok            True                  False
  INSM           73.33               15            2.33              1.98        120.54               110.68         0.787          pass              0.212             33.3                           0.422               -4.19             -0.589 downtrend_blocked_slope           False                  False
   WDC           77.78               36            0.16              0.53        461.77                85.14         0.641          pass              0.518             93.7                           0.526               -9.35             -1.254 downtrend_blocked_slope           False                  False
   XEL          100.00               14            1.18              0.64         76.89                16.83         0.553          pass              0.553             23.5                           0.486               -3.69             -0.386 downtrend_blocked_slope           False                  False
   STX           82.76               29            1.88             11.17        842.41                71.05         0.552          pass              0.330             24.7                           0.231              -14.61             -1.566 downtrend_blocked_slope           False                  False
  CSCO           66.67               15            2.06              1.62        111.46                41.41         0.548          pass              0.103              5.1                           0.190               -1.65             -0.067                      ok           False                  False
  MCHP           86.36               22            2.95              1.56         74.82                63.59         0.542          pass              0.367             20.9                           0.433               -6.91             -0.748 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         detail
2026-08-28T15:10:06.157177-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-08-28T15:05:06.122448-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-08-28T15:00:05.692919-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-08-28T14:55:06.265436-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-08-28T14:50:05.181555-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"allocated_cash": 26100.0, "asset_type": "option", "contract_symbol": "SHOP261016C00155000", "contracts": 29, "early_entry_score": 0.689, "entry_mode": "regular", "entry_option_price": 9.0, "execution_mode": "option", "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 763.0, "option_spread_pct": 6.67, "option_volume": 153.0, "success_rate": 94.59, "ticker": "SHOP", "timing_score": 0.617}
2026-08-28T14:50:05.181555-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-28", "training_samples": 5729, "window": 5}
2026-08-28T12:00:05.127019-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T11:55:02.090702-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T11:50:05.095730-04:00 early_entry_1150 early_entry_shadow {"contract_symbol": "ZS261016C00185000", "current_drop_pct": 0.64, "early_entry_score": 0.887, "early_reclaim_pct": 79.0, "entry_ask": 19.8, "entry_bid": 17.6, "entry_mode": "early", "entry_option_price": 18.7, "hypothetical_budget": 26394.05, "hypothetical_contracts": 14, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 31.0, "option_spread_pct": 11.76, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.663, "shadow_only": true, "success_rate": 95.24, "ticker": "ZS", "timing_score": 0.496, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.887, "early_reclaim_pct": 79.0, "matched_signals": 42, "recovery_stability_score": 0.663, "success_rate": 95.24, "ticker": "ZS", "timing_score": 0.496, "trend_health_status": "ok"}, {"current_drop_pct": 0.54, "early_entry_score": 0.821, "early_reclaim_pct": 67.7, "matched_signals": 35, "recovery_stability_score": 0.659, "success_rate": 97.14, "ticker": "VRTX", "timing_score": 0.514, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-28T11:45:05.139618-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "ZS261016C00185000", "current_drop_pct": 0.64, "early_entry_score": 0.887, "early_reclaim_pct": 79.0, "entry_ask": 19.6, "entry_bid": 17.6, "entry_mode": "early", "entry_option_price": 18.6, "hypothetical_budget": 26394.05, "hypothetical_contracts": 14, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 31.0, "option_spread_pct": 10.75, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.749, "shadow_only": true, "success_rate": 95.24, "ticker": "ZS", "timing_score": 0.496, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.887, "early_reclaim_pct": 79.0, "matched_signals": 42, "recovery_stability_score": 0.749, "success_rate": 95.24, "ticker": "ZS", "timing_score": 0.496, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260828153506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260828153506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260828153506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260828153506)

</details>
