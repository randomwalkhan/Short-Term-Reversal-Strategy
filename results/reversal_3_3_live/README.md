# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-13 10:30:03 EDT`
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
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$20,193.50`
- Equity: `$33,348.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$-255.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260618C00490000       2026-05-13                   0      3     13410.0                 13155.0         44.7          43.85      510.62        510.15          -255.0                   -1.9         97.14               35               0.5         52.16           51.69                  43.23                 154.0           10.0               0.12                      ok
```

## Today's Closed Trades (2026-05-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC          100.00               31            1.29              1.09        120.14               109.00         0.648          pass              0.793             62.9                           0.561               25.65              3.135                                 ok            True                   True
  TEAM           82.61               23            3.76              2.24         84.04               115.69         0.603          pass              0.317             33.3                           0.677               16.04              1.377                                 ok            True                  False
  SNPS           97.14               35            0.60              2.14        512.29                43.23         0.551          pass              0.803             60.4                           0.737                6.01              0.709                                 ok            True                   True
   ADP          100.00               11            2.17              3.25        212.42                33.54         0.550          pass              0.598             45.4                           0.426               -2.74             -0.098                                 ok            True                  False
  MSTR           90.32               31            2.28              2.95        183.16                75.69         0.503          pass              0.623             52.4                           0.760               13.92              1.264                                 ok            True                  False
  CHTR           66.67               12            3.12              3.23        146.53               118.13         0.768          pass              0.141             17.1                           0.306               -9.68             -1.381            downtrend_blocked_slope           False                  False
  INSM           76.47               34            1.14              0.92        115.60               110.65         0.595          pass              0.420             67.0                           0.377              -15.07             -2.854 downtrend_blocked_slope_and_streak           False                  False
  GEHC           60.00               25            1.43              0.62         62.02                57.10         0.574          pass              0.249             30.5                           0.313                3.22              0.336                                 ok           False                  False
  SHOP           81.82               22            2.45              1.71         99.11                84.62         0.571          pass              0.311             41.6                           0.692              -19.68             -2.525 downtrend_blocked_slope_and_streak           False                  False
  ORLY           75.00               12            1.82              1.17         91.34                35.45         0.562          pass              0.073              1.2                           0.035               -1.66             -0.542 downtrend_blocked_slope_and_streak           False                  False
  PYPL           90.00               30            0.78              0.25         45.33                37.98         0.529          pass              0.625             57.4                           0.700              -11.49             -1.416 downtrend_blocked_slope_and_streak           False                  False
  MSFT           81.82               22            1.15              3.28        406.37                32.80         0.529          pass              0.273             30.5                           0.529               -5.04             -0.220           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-05-13T10:30:03.887456-04:00 early_entry_1030           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-13T10:25:06.096694-04:00 early_entry_1025                   entry {"allocated_cash": 13410.0, "asset_type": "option", "contract_symbol": "SNPS260618C00490000", "contracts": 3, "early_entry_score": 0.822, "entry_mode": "early", "entry_option_price": 44.7, "execution_mode": "option", "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 154.0, "option_spread_pct": 12.08, "option_volume": 10.0, "success_rate": 97.14, "ticker": "SNPS", "timing_score": 0.556}
2026-05-13T10:20:06.278508-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate"}
2026-05-13T10:15:05.895485-04:00 early_entry_1015           entry_skipped                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-13T10:15:05.895485-04:00 early_entry_1015 entry_candidate_skipped                                                                                                                                                            {"early_entry_score": 0.815, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 14.0, "option_spread_pct": 21.38, "option_volume": 8.0, "reason": "no_trade_low_option_liquidity", "ticker": "TTWO", "timing_score": 0.437}
2026-05-13T10:10:06.807841-04:00 early_entry_1010           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate"}
2026-05-13T10:05:05.859086-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate"}
2026-05-13T10:00:05.846029-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate"}
2026-05-12T15:10:04.189330-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-05-12T15:05:01.045921-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260513103003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260513103003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260513103003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260513103003)

</details>
