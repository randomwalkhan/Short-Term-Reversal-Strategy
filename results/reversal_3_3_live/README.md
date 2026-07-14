# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-14 10:25:01 EDT`
Last processed slot: `manage_1030`

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

- Cash: `$17,620.25`
- Equity: `$26,940.25`
- Realized PnL: `$16,995.25`
- Unrealized PnL: `$-55.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  META     option         option META260821C00660000       2026-07-13                   1      2      9375.0                  9320.0        46.88           46.6      660.72        658.69          bid_ask_mid                       46.6                bid_ask_mid                    True           -55.0                  -0.59         81.82               22              1.27         53.38           55.71                  55.99                7322.0         1343.0               0.02                      ok
```

## Today's Closed Trades (2026-07-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   PEP           89.47               19            0.56              0.55        138.26                30.22         0.605          pass              0.459             28.8                           0.299               -0.70             -0.082                                 ok            True                  False
  AAPL           95.00               20            0.96              2.13        316.40                35.57         0.597          pass              0.689             54.1                           0.571               11.55              1.110                                 ok            True                  False
  PYPL           83.33               12            1.67              0.56         47.41                33.27         0.567          pass              0.263             34.8                           0.284                5.58              0.645                                 ok            True                  False
  PAYX          100.00               24            0.93              0.72        110.44                31.82         0.544          pass              0.775             75.8                           0.568                9.93              0.949                                 ok            True                  False
  GILD           88.46               26            0.68              0.62        131.13                32.97         0.543          pass              0.552             55.1                           0.568                3.31              0.422                                 ok            True                  False
  QCOM           81.48               27            1.67              2.15        183.06                63.33         0.535          pass              0.321             38.2                           0.280               -4.14              0.109                                 ok            True                  False
  AMGN           95.65               23            0.98              2.47        359.39                21.45         0.521          pass              0.651             37.3                           0.363               -1.01             -0.080                                 ok            True                  False
  IDXX           90.00               10            2.87             11.35        559.35                34.15         0.510          pass              0.375             19.0                           0.244                2.25              0.499                                 ok            True                  False
  CTAS           90.62               32            0.73              0.94        183.35                31.28         0.502          pass              0.658             59.4                           0.637                7.88              0.657                                 ok            True                  False
   KHC           88.89                9            1.07              0.19         25.15                36.18         0.656          pass              0.418             38.4                           0.332                3.18              0.325                                 ok           False                  False
  MDLZ          100.00                8            1.17              0.49         59.65                31.17         0.644          pass              0.551             28.9                           0.333               -0.82              0.034                                 ok           False                  False
   KDP           81.82               11            1.38              0.30         31.12                34.17         0.603          pass              0.172             18.9                           0.210               -8.00             -0.777 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-07-14T10:25:01.405128-04:00 early_entry_1025 early_entry_shadow                  {"contract_symbol": "VRSK260821C00190000", "current_drop_pct": 0.63, "early_entry_score": 0.711, "early_reclaim_pct": 79.9, "entry_ask": 12.0, "entry_bid": 9.5, "entry_mode": "early", "entry_option_price": 10.75, "hypothetical_budget": 8810.13, "hypothetical_contracts": 8, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 23.26, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.655, "shadow_only": true, "success_rate": 89.19, "ticker": "VRSK", "timing_score": 0.465, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.711, "early_reclaim_pct": 79.9, "matched_signals": 37, "recovery_stability_score": 0.655, "success_rate": 89.19, "ticker": "VRSK", "timing_score": 0.465, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-14T10:20:04.363539-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T10:15:01.411533-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T10:10:01.422460-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T10:05:01.368977-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T10:00:02.374246-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "SNPS260814C00430000", "current_drop_pct": 0.59, "early_entry_score": 0.736, "early_reclaim_pct": 81.0, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 30.45, "hypothetical_budget": 8810.13, "hypothetical_contracts": 2, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 3.0, "option_spread_pct": null, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.763, "shadow_only": true, "success_rate": 89.74, "ticker": "SNPS", "timing_score": 0.394, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.736, "early_reclaim_pct": 81.0, "matched_signals": 39, "recovery_stability_score": 0.763, "success_rate": 89.74, "ticker": "SNPS", "timing_score": 0.394, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-13T15:10:07.483451-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-13T15:05:06.913203-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-13T15:00:09.058779-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-13T14:55:09.246495-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260714102501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260714102501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260714102501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260714102501)

</details>
