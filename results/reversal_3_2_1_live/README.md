# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-14 15:30:05 EDT`
Last processed slot: `manage_1530`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while share-fallback positions also run take-profit and stop loss scans in after-hours / overnight / pre-market
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Fallback execution: buy shares when the option fails the liquidity gate; use `+3% / -3%` for common-stock fallback and `+5% / -5%` for leveraged-ETF shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; share positions can additionally trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$1,069.00`
- Equity: `$13,413.72`
- Realized PnL: `$3,145.00`
- Unrealized PnL: `$268.72`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct      option_liquidity_status
  FANG     option         option FANG260515C00185000       2026-04-14                   0      7      6160.0                 6300.00          8.8           9.00      186.41        185.56          140.00                   2.27         100.0               20              1.42         38.05           41.68                  30.53                 326.0           18.0               0.07                           ok
  REGN      share share_fallback                REGN       2026-04-13                   1      8      5916.0                 6044.72        739.5         755.59      739.50        755.59          128.72                   2.18         100.0               24              1.25           NaN             NaN                  24.22                  89.0            1.0               0.07 low_open_interest,low_volume
```

## Today's Closed Trades (2026-04-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FANG          100.00               16            1.75              2.31        188.11                30.53            True
  INTC           96.43               28            2.67              1.22         64.68                75.15            True
   XEL           95.45               22            0.56              0.32         80.31                20.44            True
  FAST           92.86               14            2.00              0.64         45.53                37.61            True
  ORLY           90.70               43            0.55              0.36         93.85                24.40            True
  CTSH           83.78               37            0.66              0.28         60.41                30.13            True
  ADBE           82.76               29            1.79              3.00        238.82                37.72            True
  PCAR           81.82               22            1.24              1.11        126.91                27.21            True
  TMUS           81.25               16            1.45              1.96        191.59                20.34            True
  WDAY           80.65               31            1.75              1.47        119.29                50.72            True
  TEAM           80.00               35            2.59              1.11         60.82                58.98            True
   HON          100.00               32            0.28              0.45        233.45                23.77           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                                                                                                                                                                                detail
2026-04-14T15:30:05.437858-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-04-14T15:25:01.440627-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-04-14T15:10:01.444585-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-04-14T15:05:06.434435-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-04-14T15:00:06.500790-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-04-14T14:55:06.427880-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-04-14T14:50:06.429660-04:00  entry_1500        entry {"allocated_cash": 6160.0, "asset_type": "option", "contract_symbol": "FANG260515C00185000", "contracts": 7, "entry_option_price": 8.8, "execution_mode": "option", "matched_signals": 20, "option_liquidity_status": "ok", "option_open_interest": 326.0, "option_spread_pct": 6.82, "option_volume": 18.0, "success_rate": 100.0, "ticker": "FANG"}
2026-04-14T14:40:05.427005-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-04-14T14:35:00.709827-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-04-14T14:30:06.440257-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260414153005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260414153005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260414153005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260414153005)

</details>
