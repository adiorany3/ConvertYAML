# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 31

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-UNKNOWN-VLESS-WS-134MS` (url=263ms, nekobox=303ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-137MS` (url=296ms, nekobox=308ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-136MS` (url=268ms, nekobox=299ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-149MS` (url=259ms, nekobox=297ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-142MS` (url=273ms, nekobox=288ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-146MS` (url=241ms, nekobox=231ms, status=no)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-149MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-151MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-139MS`
10. `AKUN-009-156-246-93-0-156-246-93-VLESS-WS-149MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-147MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-153MS` (url=243ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-149MS` (url=279ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-152MS` (url=266ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-149MS` (url=271ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-144MS` (url=257ms, status=HTTP 204)
17. `AKUN-017-ADF-VLESS-WS-155MS` (url=259ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-364MS` (url=726ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-380MS` (url=746ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-392MS` (url=745ms, status=HTTP 204)
21. `AKUN-021-SKK-VLESS-WS-385MS` (url=2131ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-396MS` (url=748ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-395MS` (url=792ms, status=HTTP 204)
24. `AKUN-025-JISON-VLESS-WS-535MS` (url=859ms, status=HTTP 204)
25. `AKUN-029-UNKNOWN-VLESS-WS-401MS` (url=867ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
