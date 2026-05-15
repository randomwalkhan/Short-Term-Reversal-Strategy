# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-15 11:35:04 EDT`
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

- Cash: `$16,120.00`
- Equity: `$31,270.00`
- Realized PnL: `$20,645.00`
- Unrealized PnL: `$625.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CDNS     option         option CDNS260618C00330000       2026-05-15                   0      5     14525.0                 15150.0        29.05           30.3       350.6        349.51          bid_ask_mid                       30.3                bid_ask_mid                    True           625.0                    4.3          97.3               37              0.63         45.67           49.12                  37.94                2023.0           40.0               0.13                      ok
```

## Today's Closed Trades (2026-05-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CDNS     option         option CDNS260618C00330000      5          2026-05-14         2026-05-15        32.35      29.115 -1617.5       -10.0 stop_loss_hit_at_scan
  SNPS     option         option SNPS260618C00490000      3          2026-05-13         2026-05-15        44.70      40.230 -1341.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           81.25               32            0.83              1.71        293.44                90.16         0.726          pass              0.474             74.0                           0.752               -1.19              0.035                                 ok            True                  False
   TXN           93.10               29            0.71              1.54        307.51                67.99         0.683          pass              0.785             80.3                           0.779                9.43              1.075                                 ok            True                  False
  SNPS          100.00               11            3.01             10.73        505.42                41.57         0.555          pass              0.492              9.9                           0.219                1.16              0.230                                 ok            True                  False
  GOOG           85.71               28            0.98              2.73        396.00                40.76         0.553          pass              0.482             51.4                           0.466                2.62              0.312                                 ok            True                  False
 GOOGL           85.71               28            0.97              2.72        399.91                40.65         0.551          pass              0.492             54.7                           0.503                2.98              0.326                                 ok            True                  False
   KDP           88.46               26            0.88              0.18         29.02                33.62         0.541          pass              0.455             22.7                           0.140               -0.84              0.071                                 ok            True                  False
  CDNS           97.14               35            0.94              2.32        351.84                37.94         0.515          pass              0.779             53.6                           0.456                2.52              0.189                                 ok            True                  False
  CHTR           63.64               11            3.49              3.62        146.45               114.29         0.696          pass              0.153             25.7                           0.185              -16.83             -1.692            downtrend_blocked_slope           False                  False
 CMCSA           87.50               24            0.68              0.12         25.12                60.26         0.682          pass              0.449             29.2                           0.212               -8.05             -0.960 downtrend_blocked_slope_and_streak           False                  False
  GEHC           55.00               20            1.81              0.79         62.33                57.53         0.591          pass              0.212             28.6                           0.299                0.83              0.195                                 ok           False                  False
  INTC          100.00                2            6.23              5.06        113.76               111.79         0.587          pass              0.540             27.1                           0.562                9.12              1.651                                 ok           False                  False
   XEL          100.00                7            1.91              1.07         79.57                24.20         0.585          pass              0.458              0.0                           0.174               -4.94             -0.347            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                            detail
2026-05-15T11:35:04.114840-04:00 early_entry_1135 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:30:01.141517-04:00 early_entry_1130 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:25:04.096857-04:00 early_entry_1125 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:20:04.254442-04:00 early_entry_1120 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:20:04.254442-04:00      manage_1130          exit {"asset_type": "option", "contract_symbol": "SNPS260618C00490000", "fill_price": 40.23, "pnl": -1341.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SNPS"}
2026-05-15T11:15:04.096489-04:00 early_entry_1115 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:10:04.211296-04:00 early_entry_1110 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:05:04.217696-04:00 early_entry_1105 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:00:05.390084-04:00 early_entry_1100 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T10:55:04.100799-04:00 early_entry_1055 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260515113504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260515113504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260515113504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260515113504)

</details>
