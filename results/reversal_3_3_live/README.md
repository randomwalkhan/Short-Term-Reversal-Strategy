# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-29 10:40:02 EDT`
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
- Equity: `$32,604.25`
- Realized PnL: `$22,264.25`
- Unrealized PnL: `$340.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   0      4     14100.0                 14440.0        35.25           36.1      477.34        478.38          bid_ask_mid                       36.1                bid_ask_mid                    True           340.0                   2.41         97.22               36              0.69         45.69           50.68                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-05-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  SOXL           92.59               27            0.98              1.55        223.97               139.09         0.777            pass              0.554              9.1                           0.184               19.46              3.744                       ok            True                  False
  INTC           95.45               22            2.49              2.11        119.99                85.20         0.579            pass              0.538              0.0                           0.157                1.68              0.987                       ok            True                  False
   TXN          100.00               15            1.65              3.65        314.39                35.59         0.541            pass              0.491              1.1                           0.227                0.83              0.486                       ok            True                  False
  AMGN           89.29               28            0.50              1.18        335.97                27.03         0.522            pass              0.572             50.6                           0.491                0.32              0.272                       ok            True                  False
  INSM           75.61               41            0.53              0.40        108.20               111.11         0.775            pass              0.453             58.4                           0.622               -6.76             -0.353  downtrend_blocked_slope           False                  False
   AEP           82.61               23            0.23              0.20        127.67                25.60         0.572            pass              0.431             72.4                           0.732               -0.88              0.122                       ok           False                  False
  AMAT           91.67               36            0.05              0.16        449.61                50.48         0.570            pass              0.738             65.4                           0.252                2.14              0.648                       ok           False                  False
  GOOG           87.50                8            1.93              5.23        383.88                41.01         0.544            pass              0.319             21.6                           0.215               -4.66             -0.356  downtrend_blocked_slope           False                  False
 GOOGL           87.50                8            2.07              5.65        387.71                41.30         0.542            pass              0.306             17.2                           0.195               -4.74             -0.347  downtrend_blocked_slope           False                  False
  MSTR           85.37               41            0.35              0.37        151.48                63.23         0.531            pass              0.650             84.5                           0.622              -19.18             -1.836  downtrend_blocked_slope           False                  False
  NXPI           93.55               31            1.01              2.35        329.27                46.79         0.499 below_threshold              0.551              0.0                           0.183               11.14              1.506                       ok           False                  False
   CSX           60.00               10            1.70              0.55         45.58                23.65         0.484 below_threshold              0.090             13.8                           0.232               -1.94             -0.010 downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-05-29T10:40:02.188936-04:00 early_entry_1040           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-29T10:35:01.212926-04:00 early_entry_1035           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-29T10:30:02.245861-04:00 early_entry_1030                   entry {"allocated_cash": 14100.0, "asset_type": "option", "contract_symbol": "SNPS260717C00470000", "contracts": 4, "early_entry_score": 0.826, "entry_mode": "early", "entry_option_price": 35.25, "execution_mode": "option", "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 115.0, "option_spread_pct": 11.06, "option_volume": 67.0, "success_rate": 97.22, "ticker": "SNPS", "timing_score": 0.401}
2026-05-29T10:25:01.208564-04:00 early_entry_1025           entry_skipped                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-29T10:25:01.208564-04:00 early_entry_1025 entry_candidate_skipped                                                                                                                                                                       {"early_entry_score": 0.814, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 51.0, "option_spread_pct": 18.61, "option_volume": 80.0, "reason": "no_trade_low_option_liquidity", "ticker": "SNPS", "timing_score": 0.395}
2026-05-29T10:20:01.218195-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-29T10:20:01.218195-04:00 early_entry_1020 entry_candidate_skipped                                                                                                                                                                       {"early_entry_score": 0.816, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 51.0, "option_spread_pct": 19.35, "option_volume": 80.0, "reason": "no_trade_low_option_liquidity", "ticker": "SNPS", "timing_score": 0.396}
2026-05-29T10:15:06.109113-04:00 early_entry_1015           entry_skipped                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-29T10:15:06.109113-04:00 early_entry_1015 entry_candidate_skipped                                                                                                                                                                             {"early_entry_score": 0.716, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 225.0, "option_spread_pct": 15.24, "option_volume": 10.0, "reason": "no_trade_low_option_liquidity", "ticker": "ALNY", "timing_score": 0.402}
2026-05-29T10:10:01.230925-04:00 early_entry_1010           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260529104002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260529104002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260529104002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260529104002)

</details>
