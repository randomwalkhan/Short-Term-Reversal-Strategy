# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-19 10:45:01 EDT`
Last processed slot: `early_entry_1045`

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
- Equity: `$27,875.00`
- Realized PnL: `$19,192.50`
- Unrealized PnL: `$-1,317.50`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PANW     option         option PANW260618C00250000       2026-05-19                   0      9     13747.5                 13680.0        15.28           15.2      245.93        245.88          bid_ask_mid                       15.2                bid_ask_mid                    True           -67.5                  -0.49         91.67               36              0.66         58.04           59.69                  42.55                2852.0           34.0               0.10                      ok
  TTWO     option         option TTWO260618C00250000       2026-05-18                   1     10     13550.0                 12300.0        13.55           12.3      241.03        239.11          bid_ask_mid                       12.3                bid_ask_mid                    True         -1250.0                  -9.23         97.62               42              0.58         61.06           60.58                  33.53                3069.0           22.0               0.11                      ok
```

## Today's Closed Trades (2026-05-19)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  NXPI           81.82               33            0.65              1.34        291.11                90.65         0.724            pass              0.482             69.1                           0.688               -0.88             -0.200                  ok            True                  False
   TXN           88.89               18            1.47              3.09        299.28                69.24         0.678            pass              0.533             58.2                           0.691                5.41              0.689                  ok            True                  False
  FTNT          100.00               38            0.72              0.64        126.23                70.72         0.620            pass              0.849             66.8                           0.501               39.67              3.247                  ok            True                  False
  GOOG           80.00               10            1.84              5.06        390.94                40.55         0.576            pass              0.118             20.3                           0.321                0.42              0.016                  ok            True                  False
 GOOGL           81.82               11            1.94              5.39        394.63                40.53         0.570            pass              0.161             16.4                           0.288                0.21              0.024                  ok            True                  False
  SNPS           96.67               30            1.20              4.20        496.63                41.65         0.537            pass              0.615              9.4                           0.100               -2.01             -0.186                  ok            True                  False
    MU           83.87               31            1.60              7.62        678.28                90.51         0.535            pass              0.485             62.9                           0.685                4.76              0.682                  ok            True                  False
  NVDA           87.50               24            1.48              2.30        221.33                44.74         0.524            pass              0.422             25.5                           0.368               11.47              1.103                  ok            True                  False
  AVGO           85.71               14            2.69              7.93        417.31                42.85         0.504            pass              0.300             23.7                           0.439               -4.21             -0.138                  ok            True                  False
  ODFL           80.00               30            0.96              1.37        203.54                43.78         0.503            pass              0.370             62.1                           0.676                3.11              0.247                  ok            True                  False
  FAST           91.67               24            0.98              0.30         43.87                22.17         0.502            pass              0.597             47.6                           0.498               -1.71             -0.203                  ok            True                  False
  MRVL          100.00               32            0.76              0.89        168.55                64.65         0.500 below_threshold              0.836             79.7                           0.650               -0.65              0.341                  ok            True                   True
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-05-19T10:45:01.038335-04:00 early_entry_1045 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:40:01.036176-04:00 early_entry_1040 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:35:03.933477-04:00 early_entry_1035 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:30:01.041969-04:00 early_entry_1030 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:25:01.081339-04:00 early_entry_1025 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:20:03.970688-04:00 early_entry_1020 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:15:01.057449-04:00 early_entry_1015 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:10:01.046495-04:00 early_entry_1010         entry {"allocated_cash": 13747.5, "asset_type": "option", "contract_symbol": "PANW260618C00250000", "contracts": 9, "early_entry_score": 0.729, "entry_mode": "early", "entry_option_price": 15.275, "execution_mode": "option", "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 2852.0, "option_spread_pct": 10.15, "option_volume": 34.0, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.462}
2026-05-19T10:05:01.031829-04:00 early_entry_1005 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-19T10:00:03.926915-04:00 early_entry_1000 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260519104501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260519104501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260519104501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260519104501)

</details>
