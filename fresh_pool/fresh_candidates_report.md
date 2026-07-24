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
1. `AKUN-001-UNKNOWN-VLESS-WS-72MS` (url=230ms, nekobox=267ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-76MS` (url=241ms, nekobox=244ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-76MS` (url=231ms, nekobox=253ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-78MS` (url=238ms, nekobox=247ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-72MS` (url=238ms, nekobox=259ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-69MS` (url=219ms, nekobox=249ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-82MS` (url=285ms, nekobox=263ms, status=yes)
8. `AKUN-008-LEVIKOGJGFDD-VLESS-WS-84MS` (url=220ms, nekobox=247ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-94MS` (url=222ms, nekobox=245ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-92MS` (url=218ms, nekobox=252ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-78MS` (url=207ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-87MS` (url=207ms, status=HTTP 204)
13. `AKUN-013-RS-RAPIDSEEDBOX-20190717-VLESS-WS-94MS` (url=231ms, status=HTTP 204)
14. `AKUN-014-ZVC-VLESS-WS-74MS` (url=224ms, status=HTTP 204)
15. `AKUN-015-ZVC-VLESS-WS-96MS` (url=206ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-138MS` (url=243ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-118MS` (url=236ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-144MS` (url=263ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-161MS` (url=292ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-155MS` (url=223ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-94MS` (url=223ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-120MS` (url=232ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-149MS` (url=367ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-354MS` (url=756ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-363MS` (url=3806ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
