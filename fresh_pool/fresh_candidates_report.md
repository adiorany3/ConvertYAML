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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-UNKNOWN-VLESS-WS-55MS` (url=212ms, nekobox=236ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-55MS` (url=211ms, nekobox=235ms, status=yes)
3. `AKUN-003-EU-VLESS-WS-75MS` (url=215ms, nekobox=242ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-68MS` (url=197ms, nekobox=239ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-80MS` (url=203ms, nekobox=253ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-64MS` (url=219ms, nekobox=239ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-125MS` (url=215ms, nekobox=245ms, status=yes)
8. `AKUN-008-FASTVPSUS-IPV4-VLESS-WS-69MS` (url=223ms, nekobox=249ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-72MS` (url=216ms, nekobox=246ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-87MS` (url=218ms, nekobox=251ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-108MS` (url=274ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-149MS` (url=279ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-151MS` (url=277ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-90MS` (url=220ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-89MS` (url=213ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-268MS` (url=553ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-539MS` (url=945ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-662MS` (url=1019ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-624MS` (url=1045ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-645MS` (url=1164ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-697MS` (url=1083ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-638MS` (url=1031ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-655MS` (url=1074ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-665MS` (url=1091ms, status=HTTP 204)
25. `AKUN-028-UNKNOWN-VLESS-WS-544MS` (url=1357ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
