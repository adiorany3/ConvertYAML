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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-88MS` (url=237ms, nekobox=237ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-88MS` (url=202ms, nekobox=274ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-86MS` (url=200ms, nekobox=260ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-87MS` (url=206ms, nekobox=231ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-92MS` (url=210ms, nekobox=232ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-95MS` (url=209ms, nekobox=249ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-95MS` (url=205ms, nekobox=236ms, status=yes)
8. `AKUN-008-TENCENT-VLESS-WS-94MS` (url=223ms, nekobox=237ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-99MS` (url=202ms, nekobox=262ms, status=yes)
10. `AKUN-010-ZVC-VLESS-WS-98MS` (url=222ms, nekobox=265ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-94MS` (url=208ms, status=HTTP 204)
12. `AKUN-012-HETZNER-VLESS-WS-94MS` (url=208ms, status=HTTP 204)
13. `AKUN-013-DIGITALOCEAN-VLESS-WS-112MS` (url=234ms, status=HTTP 204)
14. `AKUN-014-PUBLICDOMAINREGISTRY-NET-VLESS-WS-95MS` (url=207ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-96MS` (url=241ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-123MS` (url=218ms, status=HTTP 204)
17. `AKUN-017-SPEEDTEST-VLESS-WS-111MS` (url=234ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-116MS` (url=334ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-261MS` (url=3136ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-372MS` (url=819ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-382MS` (url=787ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-376MS` (url=985ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-396MS` (url=813ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-389MS` (url=792ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-415MS` (url=1145ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
