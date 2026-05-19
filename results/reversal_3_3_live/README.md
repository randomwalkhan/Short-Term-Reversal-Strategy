# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-19 11:40:06 EDT`
Last processed slot: `manage_1130`

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

- Cash: `$14,090.00`
- Equity: `$27,095.00`
- Realized PnL: `$17,837.50`
- Unrealized PnL: `$-742.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PANW     option         option PANW260618C00250000       2026-05-19                   0      9     13747.5                 13005.0        15.28          14.45      245.93         244.1          bid_ask_mid                      14.45                bid_ask_mid                    True          -742.5                   -5.4         91.67               36              0.66         58.04           59.88                  42.55                2852.0           34.0                0.1                      ok
```

## Today's Closed Trades (2026-05-19)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TTWO     option         option TTWO260618C00250000     10          2026-05-18         2026-05-19        13.55      12.195 -1355.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC          100.00               27            1.49              1.13        107.69               114.00         0.714          pass              0.801             72.0                           0.828               -1.47             -0.450                                 ok            True                  False
  GOOG           80.00               10            2.28              6.28        390.42                40.55         0.546          pass              0.076              7.2                           0.176               -0.03             -0.005                                 ok            True                  False
 GOOGL           80.00               10            2.42              6.71        394.06                40.53         0.541          pass              0.075              7.0                           0.179               -0.28              0.002                                 ok            True                  False
  SNPS           96.67               30            1.20              4.19        496.63                41.65         0.534          pass              0.658             23.6                           0.291               -2.00             -0.186                                 ok            True                  False
   KDP           88.24               34            0.53              0.11         29.38                33.71         0.518          pass              0.565             44.6                           0.238                1.23              0.239                                 ok            True                  False
  ASML           82.14               28            1.45             14.98       1465.97                50.95         0.517          pass              0.322             31.1                           0.316                0.56             -0.175                                 ok            True                  False
  KLAC           81.48               27            1.42             17.52       1748.94                51.34         0.506          pass              0.390             62.2                           0.749               -0.09             -0.038                                 ok            True                  False
  INSM           76.19               42            0.49              0.36        106.99               111.34         0.705          pass              0.498             75.7                           0.343              -23.53             -1.655 downtrend_blocked_slope_and_streak           False                  False
  QCOM          100.00                3            4.17              5.95        201.09                99.05         0.653          pass              0.563             32.6                           0.648                4.60              0.130                                 ok           False                  False
  TEAM           87.88               33            2.02              1.27         88.89               113.67         0.649          pass              0.448              6.5                           0.198               -5.12             -0.661           downtrend_blocked_streak           False                  False
  CSCO          100.00                3            2.93              2.44        117.84                49.96         0.625          pass              0.507             14.9                           0.290               22.38              2.898                                 ok           False                  False
  SHOP           83.72               43            0.24              0.18        102.31                78.89         0.613          pass              0.601             80.3                           0.386               -5.10             -0.933 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                             detail
2026-05-19T11:40:06.318992-04:00 early_entry_1140 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T11:35:01.898801-04:00 early_entry_1135 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T11:30:01.060546-04:00 early_entry_1130 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T11:25:05.065733-04:00 early_entry_1125 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T11:20:06.455937-04:00 early_entry_1120 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T11:15:01.967392-04:00 early_entry_1115 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T11:10:06.161691-04:00 early_entry_1110 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T11:05:01.947940-04:00 early_entry_1105 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T11:00:04.023655-04:00      manage_1100          exit {"asset_type": "option", "contract_symbol": "TTWO260618C00250000", "fill_price": 12.195, "pnl": -1355.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "TTWO"}
2026-05-19T11:00:04.023655-04:00 early_entry_1100 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260519114006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260519114006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260519114006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260519114006)

</details>
