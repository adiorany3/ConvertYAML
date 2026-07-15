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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-66MS` (url=224ms, nekobox=249ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-63MS` (url=245ms, nekobox=258ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-58MS` (url=207ms, nekobox=243ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-69MS` (url=218ms, nekobox=243ms, status=yes)
5. `AKUN-005-ZVC-VLESS-WS-70MS` (url=228ms, nekobox=248ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-90MS` (url=218ms, nekobox=249ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-73MS` (url=207ms, nekobox=238ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-94MS` (url=211ms, nekobox=234ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-99MS` (url=213ms, nekobox=247ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-89MS` (url=209ms, nekobox=249ms, status=yes)
11. `AKUN-011-DIXONS-VLESS-WS-81MS` (url=211ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-98MS` (url=227ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-83MS` (url=209ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-124MS` (url=195ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-132MS` (url=236ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-99MS` (url=211ms, status=HTTP 204)
17. `AKUN-017-466688-VLESS-WS-70MS` (url=224ms, status=HTTP 204)
18. `AKUN-018-WEBEX-VLESS-WS-98MS` (url=236ms, status=HTTP 204)
19. `AKUN-019-466688-VLESS-WS-116MS` (url=228ms, status=HTTP 204)
20. `AKUN-020-VOV-VLESS-WS-132MS` (url=262ms, status=HTTP 204)
21. `AKUN-021-POLICE-VLESS-WS-167MS` (url=224ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-104MS` (url=263ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-62MS` (url=226ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-246MS` (url=237ms, status=HTTP 204)
25. `AKUN-025-DEV-VLESS-WS-66MS` (url=202ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
