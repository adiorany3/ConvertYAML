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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-110MS` (url=447ms, nekobox=332ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-115MS` (url=288ms, nekobox=329ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-124MS` (url=281ms, nekobox=313ms, status=yes)
4. `AKUN-004-OVH-VLESS-WS-116MS` (url=296ms, nekobox=316ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-115MS` (url=317ms, nekobox=7173ms, status=no)
6. `AKUN-005-GO-DADDY-COM-LLC-VLESS-WS-120MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-133MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-135MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-96MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-121MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-133MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-120MS` (url=317ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-129MS` (url=333ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-181MS` (url=297ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-99MS` (url=295ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-285MS` (url=446ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-298MS` (url=611ms, status=HTTP 204)
18. `AKUN-018-RS-RAPIDSEEDBOX-20190717-VLESS-WS-244MS` (url=748ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-303MS` (url=1265ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-332MS` (url=666ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-332MS` (url=714ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-230MS` (url=434ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-335MS` (url=2742ms, status=HTTP 204)
24. `AKUN-024-ZVC-VLESS-WS-91MS` (url=417ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-548MS` (url=559ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
