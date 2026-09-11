# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-11 10:05:03 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$76,116.10`
- Equity: `$76,116.10`
- Realized PnL: `$66,116.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-11)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  MSTR     option         option MSTR261016C00130000     30          2026-09-10         2026-09-11       11.525       13.65 6375.0   18.438178 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    MU           86.84               38            0.58              3.94        975.72                56.22         0.539          pass              0.505             27.2                           0.166                3.89              0.714                                 ok            True                  False
  AMGN          100.00               18            0.93              2.49        381.40                44.93         0.640          pass              0.519              0.6                           0.123              -13.29             -1.560 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00               12            0.57              0.10         24.35                28.75         0.619          pass              0.574             33.0                           0.330               -1.96             -0.371            downtrend_blocked_slope           False                  False
  TEAM           95.12               41            0.19              0.24        179.47                63.98         0.562          pass              0.911             84.9                           0.465               -3.45             -0.705            downtrend_blocked_slope           False                  False
   PEP           90.91               22            0.05              0.05        136.63                17.04         0.560          pass              0.655             75.9                           0.383               -1.20             -0.182                                 ok           False                  False
  PANW           82.22               45            0.28              0.65        338.21                67.54         0.557          pass              0.571             85.3                           0.778              -11.83             -1.387            downtrend_blocked_slope           False                  False
  SNPS           85.71               49            0.06              0.15        397.10                60.55         0.541          pass              0.687             93.6                           0.617              -14.61             -1.569            downtrend_blocked_slope           False                  False
  CHTR           90.24               41            0.64              0.63        140.29                68.52         0.529          pass              0.721             64.8                           0.317               -5.84             -0.997            downtrend_blocked_slope           False                  False
 CMCSA           93.75               32            0.22              0.04         25.15                36.51         0.528          pass              0.763             65.7                           0.309               -4.90             -0.717 downtrend_blocked_slope_and_streak           False                  False
  AMAT           84.62               39            0.20              0.65        453.73                45.65         0.525          pass              0.600             76.9                           0.343               -6.07             -0.128           downtrend_blocked_streak           False                  False
  ADBE           97.14               35            0.77              1.34        248.26                48.95         0.512          pass              0.867             83.1                           0.864              -14.61             -1.909 downtrend_blocked_slope_and_streak           False                  False
  LRCX           81.08               37            0.89              1.86        297.21                53.83         0.502          pass              0.315             18.7                           0.214               -7.29             -0.025           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-09-11T10:05:03.681403-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:05:03.681403-04:00      manage_1000               exit                                                                                                                                                                                                                                                  {"asset_type": "option", "contract_symbol": "MSTR261016C00130000", "fill_price": 13.65, "pnl": 6375.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 18.44, "ticker": "MSTR"}
2026-09-11T10:00:03.674225-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T00:00:04.449434-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                            {'saved': 93}
2026-09-10T15:10:03.185946-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-09-10T15:05:01.362764-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-09-10T15:00:04.389376-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-09-10T14:55:01.338809-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-09-10T14:50:04.321187-04:00       entry_1500              entry {"allocated_cash": 34575.0, "asset_type": "option", "contract_symbol": "MSTR261016C00130000", "contracts": 30, "early_entry_score": 0.329, "entry_mode": "regular", "entry_option_price": 11.525, "execution_mode": "option", "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 13089.0, "option_spread_pct": 3.04, "option_volume": 181.0, "success_rate": 80.0, "ticker": "MSTR", "timing_score": 0.627}
2026-09-10T14:50:04.321187-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                             {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-10", "training_samples": 5765, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260911100503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260911100503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260911100503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260911100503)

</details>
