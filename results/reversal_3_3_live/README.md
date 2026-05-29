# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-29 10:35:01 EDT`
Last processed slot: `manage_1030`

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

- Cash: `$18,164.25`
- Equity: `$32,344.25`
- Realized PnL: `$22,264.25`
- Unrealized PnL: `$80.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   0      4     14100.0                 14180.0        35.25          35.45      477.34        479.05          bid_ask_mid                      35.45                bid_ask_mid                    True            80.0                   0.57         97.22               36              0.69         45.69           48.14                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-05-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC           97.06               34            0.68              0.57        120.64                85.20         0.637            pass              0.733             36.4                           0.178                3.57              1.071                                 ok            True                  False
   TXN          100.00               28            0.70              1.54        315.29                35.59         0.524            pass              0.572              0.0                           0.269                1.81              0.529                                 ok            True                  False
  INSM           75.61               41            0.60              0.45        108.18               111.11         0.772            pass              0.435             52.6                           0.438               -6.83             -0.356            downtrend_blocked_slope           False                  False
  MELI           93.02               43            0.08              0.99       1695.11                61.27         0.607            pass              0.881             90.9                           0.499                5.40              0.823                                 ok           False                  False
   AEP           78.95               19            0.34              0.31        127.63                25.60         0.587            pass              0.293             58.1                           0.628               -1.00              0.116                                 ok           False                  False
 GOOGL           90.00               10            1.83              5.00        387.99                41.30         0.546            pass              0.401             26.7                           0.261               -4.51             -0.336            downtrend_blocked_slope           False                  False
  GOOG           91.67               12            1.74              4.70        384.11                41.01         0.534            pass              0.466             29.5                           0.273               -4.47             -0.347            downtrend_blocked_slope           False                  False
  MSTR           85.37               41            0.36              0.38        151.48                63.23         0.530            pass              0.648             84.1                           0.551              -19.18             -1.836            downtrend_blocked_slope           False                  False
  REGN           90.70               43            0.08              0.33        621.38                44.05         0.521            pass              0.816             92.8                           0.717              -12.75             -1.042 downtrend_blocked_slope_and_streak           False                  False
  AMGN           91.18               34            0.27              0.64        336.21                27.03         0.498 below_threshold              0.728             73.4                           0.761                0.56              0.283                                 ok           False                  False
   CSX           60.00               10            1.66              0.53         45.58                23.65         0.487 below_threshold              0.097             16.0                           0.283               -1.89             -0.008           downtrend_blocked_streak           False                  False
   ADI           89.29               28            1.05              3.08        417.69                39.51         0.484 below_threshold              0.515             32.9                           0.246               -2.86             -0.107                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-05-29T10:35:01.212926-04:00 early_entry_1035           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-29T10:30:02.245861-04:00 early_entry_1030                   entry {"allocated_cash": 14100.0, "asset_type": "option", "contract_symbol": "SNPS260717C00470000", "contracts": 4, "early_entry_score": 0.826, "entry_mode": "early", "entry_option_price": 35.25, "execution_mode": "option", "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 115.0, "option_spread_pct": 11.06, "option_volume": 67.0, "success_rate": 97.22, "ticker": "SNPS", "timing_score": 0.401}
2026-05-29T10:25:01.208564-04:00 early_entry_1025           entry_skipped                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-29T10:25:01.208564-04:00 early_entry_1025 entry_candidate_skipped                                                                                                                                                                       {"early_entry_score": 0.814, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 51.0, "option_spread_pct": 18.61, "option_volume": 80.0, "reason": "no_trade_low_option_liquidity", "ticker": "SNPS", "timing_score": 0.395}
2026-05-29T10:20:01.218195-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-29T10:20:01.218195-04:00 early_entry_1020 entry_candidate_skipped                                                                                                                                                                       {"early_entry_score": 0.816, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 51.0, "option_spread_pct": 19.35, "option_volume": 80.0, "reason": "no_trade_low_option_liquidity", "ticker": "SNPS", "timing_score": 0.396}
2026-05-29T10:15:06.109113-04:00 early_entry_1015           entry_skipped                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-29T10:15:06.109113-04:00 early_entry_1015 entry_candidate_skipped                                                                                                                                                                             {"early_entry_score": 0.716, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 225.0, "option_spread_pct": 15.24, "option_volume": 10.0, "reason": "no_trade_low_option_liquidity", "ticker": "ALNY", "timing_score": 0.402}
2026-05-29T10:10:01.230925-04:00 early_entry_1010           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate"}
2026-05-29T10:05:04.226067-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_trade_after_option_and_timing_filters"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260529103501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260529103501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260529103501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260529103501)

</details>
