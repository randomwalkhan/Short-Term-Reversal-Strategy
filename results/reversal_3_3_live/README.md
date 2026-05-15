# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-15 15:45:04 EDT`
Last processed slot: `manual`

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

- Cash: `$16,120.00`
- Equity: `$30,670.00`
- Realized PnL: `$20,645.00`
- Unrealized PnL: `$25.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CDNS     option         option CDNS260618C00330000       2026-05-15                   0      5     14525.0                 14550.0        29.05           29.1       350.6        348.45          bid_ask_mid                       29.1                bid_ask_mid                    True            25.0                   0.17          97.3               37              0.63         45.67           46.81                  37.94                2023.0           40.0               0.13                      ok
```

## Today's Closed Trades (2026-05-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CDNS     option         option CDNS260618C00330000      5          2026-05-14         2026-05-15        32.35      29.115 -1617.5       -10.0 stop_loss_hit_at_scan
  SNPS     option         option SNPS260618C00490000      3          2026-05-13         2026-05-15        44.70      40.230 -1341.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           81.82               33            0.76              1.56        293.50                90.16         0.725            pass              0.503             76.3                           0.596               -1.12              0.039                                 ok            True                  False
   TXN           90.00               20            1.45              3.12        306.83                67.99         0.691            pass              0.583             60.1                           0.413                8.62              1.042                                 ok            True                  False
 GOOGL           84.00               25            1.07              3.00        399.78                40.65         0.562            pass              0.413             49.9                           0.567                2.88              0.321                                 ok            True                  False
  GOOG           85.19               27            1.02              2.84        395.95                40.76         0.556            pass              0.455             49.4                           0.556                2.58              0.310                                 ok            True                  False
  CDNS           96.67               30            1.24              3.07        351.52                37.94         0.529            pass              0.702             38.7                           0.462                2.20              0.175                                 ok            True                  False
  SNPS           96.00               25            1.73              6.18        507.37                41.57         0.528            pass              0.713             53.5                           0.670                2.49              0.290                                 ok            True                  False
  MDLZ           82.61               23            0.81              0.35         60.82                21.64         0.501            pass              0.286             26.7                           0.295               -1.46             -0.088                                 ok            True                  False
   STX           94.44               36            0.80              4.52        802.82                56.74         0.500 below_threshold              0.859             83.4                           0.616                9.82              1.025                                 ok            True                   True
 CMCSA           90.00               10            1.61              0.28         25.05                60.26         0.705            pass              0.348              3.6                           0.246               -8.92             -1.003 downtrend_blocked_slope_and_streak           False                  False
  CHTR           66.67                3            5.46              5.65        145.58               114.29         0.599            pass              0.147             29.0                           0.542              -18.53             -1.785            downtrend_blocked_slope           False                  False
  INTC          100.00                2            6.15              4.99        113.79               111.79         0.592            pass              0.543             28.1                           0.275                9.22              1.655                                 ok           False                  False
   XEL          100.00                2            2.36              1.32         79.46                24.20         0.578            pass              0.516             19.6                           0.346               -5.38             -0.368            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-15T15:10:01.306366-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-15T15:05:04.259285-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-15T15:00:04.164689-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-15T14:55:04.243758-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-15T14:50:02.185201-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-15T14:50:02.185201-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-15", "training_samples": 5061, "window": 5}
2026-05-15T12:00:02.263118-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-15T11:55:05.834638-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-15T11:50:01.284692-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-15T11:45:04.258436-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260515154504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260515154504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260515154504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260515154504)

</details>
