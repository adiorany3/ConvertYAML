# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 21
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 25

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
1. `AKUN-001-UNKNOWN-VLESS-WS-69MS` (url=205ms, nekobox=241ms, status=yes)
2. `AKUN-002-LEVIKOGJGFDD-VLESS-WS-72MS`
3. `AKUN-003-UNKNOWN-VLESS-WS-78MS`
4. `AKUN-004-UNKNOWN-VLESS-WS-87MS`
5. `AKUN-005-ZVC-VLESS-WS-92MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-79MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-88MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-83MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-95MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-107MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-95MS` (url=208ms, status=HTTP 204)
12. `AKUN-013-OPENAI-VLESS-WS-102MS` (url=204ms, status=HTTP 204)
13. `AKUN-015-UNKNOWN-VLESS-WS-124MS` (url=349ms, status=HTTP 204)
14. `AKUN-016-UNKNOWN-VLESS-WS-97MS` (url=228ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-133MS` (url=405ms, status=HTTP 204)
16. `AKUN-018-UNKNOWN-VLESS-WS-145MS` (url=357ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-123MS` (url=378ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-180MS` (url=246ms, status=HTTP 204)
19. `AKUN-022-CLOUDFLARE-VLESS-WS-646MS` (url=1114ms, status=HTTP 204)
20. `AKUN-034-CLOUDFLARE-VLESS-WS-851MS` (url=1323ms, status=HTTP 204)
21. `AKUN-035-UNKNOWN-VLESS-WS-855MS` (url=1395ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
