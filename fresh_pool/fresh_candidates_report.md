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
1. `AKUN-001-UNKNOWN-VLESS-WS-63MS` (url=219ms, nekobox=235ms, status=yes)
2. `AKUN-002-GO-DADDY-COM-LLC-VLESS-WS-72MS` (url=216ms, nekobox=243ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-71MS` (url=200ms, nekobox=236ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-68MS` (url=195ms, nekobox=236ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-68MS` (url=214ms, nekobox=247ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-73MS` (url=219ms, nekobox=254ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-77MS` (url=209ms, nekobox=247ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-69MS` (url=212ms, nekobox=257ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-71MS` (url=198ms, nekobox=227ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-84MS` (url=199ms, nekobox=225ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-94MS` (url=219ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-77MS` (url=213ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-72MS` (url=213ms, status=HTTP 204)
14. `AKUN-014-WEBEX-VLESS-WS-82MS` (url=196ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-88MS` (url=216ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-78MS` (url=219ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-83MS` (url=223ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-81MS` (url=213ms, status=HTTP 204)
19. `AKUN-019-DEV-VLESS-WS-118MS` (url=198ms, status=HTTP 204)
20. `AKUN-020-NEXUSMODS-VLESS-WS-111MS` (url=216ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-120MS` (url=204ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-122MS` (url=228ms, status=HTTP 204)
23. `AKUN-023-DEV-VLESS-WS-124MS` (url=208ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-101MS` (url=211ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-102MS` (url=215ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
