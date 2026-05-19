# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-19 10:50:05 EDT`
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
- Equity: `$27,882.50`
- Realized PnL: `$19,192.50`
- Unrealized PnL: `$-1,310.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PANW     option         option PANW260618C00250000       2026-05-19                   0      9     13747.5                 13387.5        15.28          14.88      245.93        245.90          bid_ask_mid                      14.88                bid_ask_mid                    True          -360.0                  -2.62         91.67               36              0.66         58.04           58.46                  42.55                2852.0           34.0               0.10                      ok
  TTWO     option         option TTWO260618C00250000       2026-05-18                   1     10     13550.0                 12600.0        13.55          12.60      241.03        239.04          bid_ask_mid                      12.60                bid_ask_mid                    True          -950.0                  -7.01         97.62               42              0.58         61.06           61.77                  33.53                3069.0           22.0               0.11                      ok
```

## Today's Closed Trades (2026-05-19)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           81.25               32            0.81              1.66        290.97                90.65         0.721          pass              0.437             61.7                           0.509               -1.04             -0.207                                 ok            True                  False
   TXN           91.67               12            1.84              3.87        298.94                69.24         0.696          pass              0.537             47.6                           0.483                5.01              0.672                                 ok            True                  False
  FTNT          100.00               34            0.83              0.74        126.18                70.72         0.638          pass              0.809             61.7                           0.466               39.51              3.242                                 ok            True                  False
  GOOG           80.00               10            2.00              5.49        390.76                40.55         0.566          pass              0.097             13.4                           0.258                0.26              0.008                                 ok            True                  False
 GOOGL           80.00               10            2.16              5.99        394.37                40.53         0.560          pass              0.077              7.1                           0.215               -0.01              0.014                                 ok            True                  False
    MU           84.85               33            1.32              6.31        678.83                90.51         0.541          pass              0.544             69.2                           0.749                5.05              0.694                                 ok            True                  False
  SNPS           96.30               27            1.42              4.96        496.31                41.65         0.540          pass              0.596              9.7                           0.196               -2.22             -0.196                                 ok            True                  False
  NVDA           89.29               28            1.21              1.88        221.51                44.74         0.517          pass              0.536             39.0                           0.464               11.77              1.115                                 ok            True                  False
  FAST           91.30               23            1.00              0.31         43.87                22.17         0.507          pass              0.578             46.3                           0.494               -1.74             -0.204                                 ok            True                  False
  TEAM           90.91               44            0.43              0.27         89.32               113.67         0.696          pass              0.701             46.9                           0.242               -3.57             -0.588           downtrend_blocked_streak           False                  False
  INTC          100.00               14            3.91              2.96        106.90               114.00         0.652          pass              0.572             26.8                           0.445               -3.89             -0.563 downtrend_blocked_slope_and_streak           False                  False
  MNST           63.64               11            1.93              1.20         88.03                49.83         0.610          pass              0.092              8.1                           0.296               14.55              1.473                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-05-19T10:50:05.059636-04:00 early_entry_1050 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:45:01.038335-04:00 early_entry_1045 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:40:01.036176-04:00 early_entry_1040 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:35:03.933477-04:00 early_entry_1035 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:30:01.041969-04:00 early_entry_1030 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:25:01.081339-04:00 early_entry_1025 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:20:03.970688-04:00 early_entry_1020 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:15:01.057449-04:00 early_entry_1015 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:10:01.046495-04:00 early_entry_1010         entry {"allocated_cash": 13747.5, "asset_type": "option", "contract_symbol": "PANW260618C00250000", "contracts": 9, "early_entry_score": 0.729, "entry_mode": "early", "entry_option_price": 15.275, "execution_mode": "option", "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 2852.0, "option_spread_pct": 10.15, "option_volume": 34.0, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.462}
2026-05-19T10:05:01.031829-04:00 early_entry_1005 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260519105005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260519105005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260519105005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260519105005)

</details>
