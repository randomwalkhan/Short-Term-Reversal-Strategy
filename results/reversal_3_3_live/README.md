# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-19 10:55:01 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$1,895.00`
- Equity: `$27,972.50`
- Realized PnL: `$19,192.50`
- Unrealized PnL: `$-1,220.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PANW     option         option PANW260618C00250000       2026-05-19                   0      9     13747.5                 13477.5        15.28          14.98      245.93        245.66          bid_ask_mid                      14.98                bid_ask_mid                    True          -270.0                  -1.96         91.67               36              0.66         58.04           59.27                  42.55                2852.0           34.0               0.10                      ok
  TTWO     option         option TTWO260618C00250000       2026-05-18                   1     10     13550.0                 12600.0        13.55          12.60      241.03        238.94          bid_ask_mid                      12.60                bid_ask_mid                    True          -950.0                  -7.01         97.62               42              0.58         61.06           62.18                  33.53                3069.0           22.0               0.11                      ok
```

## Today's Closed Trades (2026-05-19)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           82.35               34            0.51              1.05        291.23                90.65         0.727          pass              0.523             75.7                           0.660               -0.74             -0.193                                 ok            True                  False
   TXN           90.00               20            1.36              2.86        299.38                69.24         0.674          pass              0.585             61.3                           0.631                5.52              0.694                                 ok            True                  False
  GOOG           80.00               10            1.83              5.04        390.95                40.55         0.576          pass              0.119             20.5                           0.259                0.43              0.016                                 ok            True                  False
 GOOGL           81.82               11            1.97              5.47        394.59                40.53         0.568          pass              0.157             15.1                           0.222                0.18              0.023                                 ok            True                  False
    MU           85.29               34            0.98              4.69        679.53                90.51         0.558          pass              0.588             77.2                           0.892                5.41              0.710                                 ok            True                  False
  SNPS           96.30               27            1.39              4.84        496.36                41.65         0.542          pass              0.603             11.9                           0.144               -2.19             -0.194                                 ok            True                  False
  NVDA           89.29               28            1.12              1.74        221.58                44.74         0.523          pass              0.551             43.8                           0.512               11.88              1.120                                 ok            True                  False
  ASML           82.14               28            1.43             14.75       1466.07                50.95         0.518          pass              0.326             32.2                           0.365                0.58             -0.174                                 ok            True                  False
  FAST           91.30               23            1.05              0.32         43.86                22.17         0.504          pass              0.570             43.9                           0.454               -1.78             -0.206                                 ok            True                  False
  TEAM           90.91               44            0.49              0.30         89.30               113.67         0.692          pass              0.680             40.0                           0.216               -3.63             -0.590           downtrend_blocked_streak           False                  False
  INTC          100.00               15            3.53              2.67        107.02               114.00         0.668          pass              0.602             33.8                           0.511               -3.51             -0.545 downtrend_blocked_slope_and_streak           False                  False
  SHOP           83.72               43            0.04              0.03        102.38                78.89         0.626          pass              0.653             97.0                           0.419               -4.90             -0.924 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-05-19T10:55:01.036439-04:00 early_entry_1055 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:50:05.059636-04:00 early_entry_1050 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:45:01.038335-04:00 early_entry_1045 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:40:01.036176-04:00 early_entry_1040 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:35:03.933477-04:00 early_entry_1035 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:30:01.041969-04:00 early_entry_1030 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:25:01.081339-04:00 early_entry_1025 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:20:03.970688-04:00 early_entry_1020 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:15:01.057449-04:00 early_entry_1015 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:10:01.046495-04:00 early_entry_1010         entry {"allocated_cash": 13747.5, "asset_type": "option", "contract_symbol": "PANW260618C00250000", "contracts": 9, "early_entry_score": 0.729, "entry_mode": "early", "entry_option_price": 15.275, "execution_mode": "option", "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 2852.0, "option_spread_pct": 10.15, "option_volume": 34.0, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.462}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260519105501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260519105501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260519105501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260519105501)

</details>
