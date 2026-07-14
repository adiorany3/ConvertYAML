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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-87MS` (url=235ms, nekobox=264ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-97MS` (url=218ms, nekobox=240ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-93MS` (url=207ms, nekobox=241ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-98MS` (url=208ms, nekobox=239ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-95MS` (url=216ms, nekobox=234ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-101MS` (url=230ms, nekobox=272ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-98MS` (url=222ms, nekobox=282ms, status=yes)
8. `AKUN-008-IONOS-VLESS-WS-100MS` (url=229ms, nekobox=234ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-116MS` (url=211ms, nekobox=236ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-112MS` (url=228ms, nekobox=273ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-123MS` (url=246ms, status=HTTP 204)
12. `AKUN-012-PUBLICDOMAINREGISTRY-NET-VLESS-WS-100MS` (url=216ms, status=HTTP 204)
13. `AKUN-013-MEDIUM-VLESS-WS-134MS` (url=271ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-146MS` (url=248ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-160MS` (url=232ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-118MS` (url=212ms, status=HTTP 204)
17. `AKUN-017-VOV-VLESS-WS-139MS` (url=224ms, status=HTTP 204)
18. `AKUN-018-MYBB-VLESS-WS-114MS` (url=230ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-143MS` (url=225ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-116MS` (url=241ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-185MS` (url=362ms, status=HTTP 204)
22. `AKUN-022-VOV-VLESS-WS-150MS` (url=322ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-121MS` (url=336ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-150MS` (url=210ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-111MS` (url=235ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
