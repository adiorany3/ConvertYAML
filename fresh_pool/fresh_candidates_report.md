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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-93MS` (url=291ms, nekobox=192ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-109MS`
3. `AKUN-002-UNKNOWN-VLESS-WS-115MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-196MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-117MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-103MS` (url=263ms, nekobox=204ms, status=no)
7. `AKUN-005-CLOUDFLARE-VLESS-WS-124MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-94MS`
9. `AKUN-007-UNKNOWN-VLESS-WS-109MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-98MS` (url=273ms, nekobox=205ms, status=no)
11. `AKUN-008-CLOUDFLARE-VLESS-WS-93MS`
12. `AKUN-009-CLOUDFLARE-VLESS-WS-107MS`
13. `AKUN-010-ZVC-VLESS-WS-150MS`
14. `AKUN-014-CLOUDFLARE-VLESS-WS-110MS` (url=297ms, status=HTTP 204)
15. `AKUN-015-SC-APHRODITEGROUP-201910-VLESS-WS-103MS` (url=451ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-158MS` (url=261ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-282MS` (url=447ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-148MS` (url=353ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-185MS` (url=344ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-193MS` (url=497ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-351MS` (url=627ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-316MS` (url=495ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-389MS` (url=1057ms, status=HTTP 204)
24. `AKUN-025-090227-VLESS-WS-456MS` (url=357ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-337MS` (url=281ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
