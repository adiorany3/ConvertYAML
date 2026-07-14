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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-59MS` (url=213ms, nekobox=242ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-63MS` (url=211ms, nekobox=257ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-66MS` (url=209ms, nekobox=239ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-73MS` (url=216ms, nekobox=242ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-64MS` (url=204ms, nekobox=227ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-77MS` (url=220ms, nekobox=247ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-84MS` (url=206ms, nekobox=238ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-89MS` (url=244ms, nekobox=255ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-93MS` (url=227ms, nekobox=251ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-85MS` (url=206ms, nekobox=256ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-93MS` (url=222ms, status=HTTP 204)
12. `AKUN-012-VOV-VLESS-WS-102MS` (url=215ms, status=HTTP 204)
13. `AKUN-013-SPEEDTEST-VLESS-WS-105MS` (url=225ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-110MS` (url=214ms, status=HTTP 204)
15. `AKUN-015-DEV-VLESS-WS-95MS` (url=211ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-76MS` (url=200ms, status=HTTP 204)
17. `AKUN-018-SPEEDTEST-VLESS-WS-100MS` (url=212ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-78MS` (url=210ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-114MS` (url=208ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-104MS` (url=220ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-113MS` (url=228ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-64MS` (url=237ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-72MS` (url=223ms, status=HTTP 204)
24. `AKUN-025-WEBEX-VLESS-WS-92MS` (url=226ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-85MS` (url=222ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
