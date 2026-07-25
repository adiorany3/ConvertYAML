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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-UNKNOWN-VLESS-WS-56MS` (url=208ms, nekobox=222ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-62MS` (url=197ms, nekobox=233ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-67MS` (url=209ms, nekobox=226ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-56MS` (url=199ms, nekobox=222ms, status=yes)
5. `AKUN-005-DEV-VLESS-WS-72MS` (url=222ms, nekobox=243ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-71MS` (url=198ms, nekobox=223ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-69MS` (url=198ms, nekobox=236ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-78MS` (url=199ms, nekobox=229ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-93MS` (url=198ms, nekobox=171ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-86MS`
11. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-87MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-65MS` (url=211ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-109MS` (url=200ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-77MS` (url=199ms, status=HTTP 204)
15. `AKUN-015-DEV-VLESS-WS-92MS` (url=210ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-60MS` (url=206ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-118MS` (url=211ms, status=HTTP 204)
18. `AKUN-018-EU-VLESS-WS-119MS` (url=208ms, status=HTTP 204)
19. `AKUN-019-DEV-VLESS-WS-114MS` (url=214ms, status=HTTP 204)
20. `AKUN-020-ZVC-VLESS-WS-101MS` (url=230ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-91MS` (url=210ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-109MS` (url=204ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-168MS` (url=224ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-212MS` (url=468ms, status=HTTP 204)
25. `AKUN-025-LT-LRTC-20060503-VLESS-WS-218MS` (url=497ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
